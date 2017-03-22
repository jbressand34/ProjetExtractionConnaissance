package package1;

import weka.core.Attribute;
import weka.core.DenseInstance;
import weka.core.FastVector;
//import weka.core.FastVector;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.converters.ArffSaver;
import weka.core.converters.CSVLoader;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class TextDirectoryToArff {
	public void createDataset(String directoryPath) throws Exception {

		FastVector atts = new FastVector(2);
		atts.addElement(new Attribute("texte", (FastVector) null));
		atts.addElement(new Attribute("valeur", (FastVector) null));
		Instances data = new Instances(
				"Classification de documents par opinion", atts, 0);

		File dir = new File(directoryPath);
		String[] files = dir.list();
		String s, s1;

		if (files[0].endsWith(".txt") && files[1].endsWith(".txt")) {
			try {
				File txt = new File(directoryPath + File.separator + files[0]);
				File txt1 = new File(directoryPath + File.separator + files[1]);
				InputStreamReader is, is1;
				is = new InputStreamReader(new FileInputStream(txt));
				is1 = new InputStreamReader(new FileInputStream(txt1));
				BufferedReader br = new BufferedReader(is);
				BufferedReader br1 = new BufferedReader(is1);
				File fout = new File("out.arff");
				FileOutputStream fos = new FileOutputStream(fout);
				BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
				bw.write(data.toString());

				while ((s = br.readLine()) != null
						&& (s1 = br1.readLine()) != null) {
					String dataOut = "\"" + s + "\"," + s1;
					bw.write(dataOut);
					bw.newLine();
				}

				bw.close();
				is.close();
				is1.close();
			} catch (Exception e) {
				System.err.println("failed to convert file: " + directoryPath
						+ File.separator + files[0]);
			}
		}

	}

	public static void main(String[] args) {
		TextDirectoryToArff tdta = new TextDirectoryToArff();
		try {
			tdta.createDataset("/home/anastasiia/workspace_new/EDC/src/package1/Dataset");
		} catch (Exception e) {
			System.err.println(e.getMessage());
			e.printStackTrace();
		}

	}
}
