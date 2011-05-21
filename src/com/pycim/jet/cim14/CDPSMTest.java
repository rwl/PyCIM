package com.pycim.jet.cim14;

import java.net.URL;
import java.util.HashMap;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.FileLocator;
import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.core.runtime.IStatus;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.Platform;
import org.eclipse.core.runtime.Status;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.jet.JET2Platform;
import org.osgi.framework.Bundle;

import com.pycim.jet.Activator;

import junit.framework.TestCase;

public class CDPSMTest extends TestCase {

	private final String base = "Model/CIM14/CDPSM/";
	private final Path balancedPath = new Path(base + "Balanced.ecore");

	private final String projectName = "PyCIM";

	/** JET transform ID. */
	private final String transformId = "com.github.enerate.python";

	/** Progress monitor for the transformation. */
	IProgressMonitor monitor = new NullProgressMonitor();

	public CDPSMTest(String name) {
		super(name);
	}

	protected void setUp() throws Exception {
		super.setUp();
	}

	public void testCDPSM() {

		Bundle bundle = Activator.getContext().getBundle();
		URL balancedURL = FileLocator.find(bundle, balancedPath, null);


        ResourceSet metaResourceSet = new ResourceSetImpl();
        Resource metaResource = metaResourceSet.createResource(URI.createURI(balancedURL.getPath()));

//		IProject project = ResourcesPlugin.getWorkspace().getRoot().getProject(projectName);

		final HashMap<String, String> variables = new HashMap<String, String>();
		variables.put("org.eclipse.jet.resource.project.name", projectName);



//		IStatus status = JET2Platform.runTransformOnResource(transformId, project.getFile(balancedPath), variables, monitor);
		IStatus status = JET2Platform.runTransformOnObject(transformId, metaResource, variables, monitor);

		assertTrue(status == Status.OK_STATUS);
	}

}
