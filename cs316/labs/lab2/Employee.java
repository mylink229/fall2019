public class Employee {
    private final String firstName;                        
    private final String lastName;                         
    private final String socialSecurityNumber;             

    public Employee(String firstName, String lastname, String socialSecurityNumber) {
        this.firstName = firstName;
        this.lastName = lastname;
        this.socialSecurityNumber = socialSecurityNumber;
    }

    public String getFname() {
        return this.fName;
    }

    public String getLname() {
        return this.lName;
    }

    public String getSSN() {
        return this.ssn;
    }

    public String toString() {                                           
        return String.format("%s: %s %s%n%s: %s%n%s: %.2f%n%s: %.2f",     
            "commission employee", firstName, lastName,                    
            "social security number", socialSecurityNumber);
    }                                                                    
}