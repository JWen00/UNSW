import java.time.LocalDate;


public class BankAccount { 
    private int currentBalance; // Invariance >= 0
    private int dailyWithdrawal; // Invariance <= 800
    private LocalDate currentDate; 

    public BankAccount() { 
        this.currentBalance = 0;
        this.dailyWithdrawal = 0;
        this.currentDate = LocalDate.now();
    }

    public boolean withdraw(int amount) {
        
        // Check the limit
        if (amount > this.currentBalance || amount < 0) { 
            return false;
        }

        // Check the daily withdrawal 
        if (!currentDate.equals(LocalDate.now())) { 
            currentDate = LocalDate.now(); 
            dailyWithdrawal = 0;
        }

        // Check daily limit 
        if (amount + dailyWithdrawal > 800) { 
            return false;
        }
        this.currentBalance -= amount;
        this.dailyWithdrawal += amount;
        return true;
    }

    public boolean deposit(int amount) { 
        if (amount < 0) { 
            return false;
        }

        this.currentBalance += amount;
        return true;
    }
}


public class SavingsAccount extends BankAccount { 

    public boolean withdraw(int amount) {
        if (amount > 200) { 
            return false; 
        }

        return super.withdraw(amount);
    }
}


/* 
Precondition:  what you require for the program (Assume) 
Postcondition: garuntee about the ouput from our assumption 
Class Invariant: Things that don't change
*/