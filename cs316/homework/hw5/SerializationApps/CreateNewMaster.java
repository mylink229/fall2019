import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.NoSuchElementException;
import java.io.BufferedReader;      
import java.util.Scanner;
import javax.xml.bind.JAXB;
import java.util.List;

public class CreateNewMaster {
   public static void main(String[] args) {
      // open clients.xml, write objects to it then close file
      try(BufferedWriter output = 
         Files.newBufferedWriter(Paths.get("newMaster.xml"))) {
         
         Scanner input = new Scanner(System.in);

         Accounts newAccounts = new Accounts(); 
         List <Account> oldAccounts = getOldAccounts().getAccounts(); 
         List <Account> trans = getTransactions().getAccounts(); 

         for (int i = 0; i < oldAccounts.size(); i++) { 
            for (int j = 0; j < trans.size(); j++) {
               if (oldAccounts.get(i).getAccountNumber() == trans.get(j).getAccountNumber()) {
                  System.out.println("--MATCH--");
                  double bal1 = oldAccounts.get(i).getBalance();
                  double bal2 = trans.get(j).getBalance();
                  double diff = bal1 - bal2;

                  Account acc = new Account(
                     oldAccounts.get(i).getAccountNumber(),
                     oldAccounts.get(i).getFirstName(),
                     oldAccounts.get(i).getLastName(),
                     diff
                  );

                  newAccounts.getAccounts().add(acc);
               }
            }
         }
         // write AccountList's XML to output
         JAXB.marshal(newAccounts, output); 
      }
      catch (IOException ioException) {
         System.err.println("Error opening file. Terminating.");
      } 
   } 

   public static Accounts getTransactions() {
      Accounts transactions = null;
      try(BufferedReader input = 
         Files.newBufferedReader(Paths.get("trans.xml"))) {
         // unmarshal the file's contents
         transactions = JAXB.unmarshal(input, Accounts.class);
         
         System.out.println("--TRANS != NULL");
         return transactions;
      } 
      catch (IOException ioException) {
         System.err.println("Error opening file.");
      } 
      System.out.println("--TRANS = NULL");
      return transactions;
   }

   public static Accounts getOldAccounts() {
      Accounts accounts = null;
      try(BufferedReader input = 
         Files.newBufferedReader(Paths.get("oldMaster.xml"))) {
         // unmarshal the file's contents
         accounts = JAXB.unmarshal(input, Accounts.class);
         
         System.out.println("--OLD ACCCOUNTS != NULL");
         return accounts;
      } 
      catch (IOException ioException) {
         System.err.println("Error opening file.");
      } 
      System.out.println("--OLD ACCCOUNTS = NULL");
      return accounts;
   }
} 