package package1;

import weka.core.Attribute;
import weka.core.FastVector;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.converters.ArffSaver;
import weka.core.converters.CSVLoader;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class CSV2Arff {
  /**
   * takes 2 arguments:
   * - CSV input file
   * - ARFF output file
 * @throws IOException 
   */
  public static void main(String[] args) throws IOException{
 
    // load CSV
    CSVLoader loader = new CSVLoader();
    loader.setSource(new File("labels.csv"));
    Instances data = loader.getDataSet();
 
    BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("dataset.txt")));
    
    String ligne;
    int numeroInstance = 0;
    Instance instance = null;
    ArrayList<Attribute> mesAttributs = new ArrayList<Attribute>();
    mesAttributs.add(new Attribute("texte"));
    mesAttributs.add(new Attribute("valeur"));
    
    Instances dataArff = new Instances("mesInstances",mesAttributs, 20000);
    
 // save ARFF
    ArffSaver saver = new ArffSaver();
    saver.setFile(new File("output.arff"));
    saver.setDestination(new File("output.arff"));
    
    while((ligne=br.readLine())!=null){
    	instance = data.instance(numeroInstance);
    	String valeur = instance.stringValue(0);
    	instance.deleteAttributeAt(0);
    	instance.setValue(new Attribute("texte"), ligne);
    	instance.setValue(new Attribute("valeur"), valeur);
    	dataArff.add(instance);
    	
    	numeroInstance++;
    }
    
    saver.setInstances(data);
    saver.writeBatch();
  }
}

