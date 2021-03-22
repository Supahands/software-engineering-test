import java.sql.Timestamp;    
import java.util.Date;    
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.text.ParseException;  

class Solution {
    
    /**
     * Helper function to calculate the difference between the two date objects 
     * based on the date only and ignoring the time
     */
    public static long diffInDays(Date newDate, Date prevDate) {
        long diffInMillies = 0;
        try {
            DateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
            newDate = formatter.parse(formatter.format(newDate));
            prevDate = formatter.parse(formatter.format(prevDate));
            diffInMillies = Math.abs(newDate.getTime() - prevDate.getTime());
        } catch(ParseException e) {
            e.printStackTrace();
        }
        return (diffInMillies / (1000 * 60 * 60 * 24)) % 365; 
    }
    
    /***
     * This method is to get the longest consecutive login (considering only dates and not time)
     * timeStamps accepts the list of all the logins as String array
     * returns longest consecutive login
     */
    public static int getLongestConsecutiveLogin(String[] timeStamps) {
        Date prevLogin = null;
        
        int longestConsecutiveLogin = 0;
        int consecutiveLogin = 1;
        String maxDates = "";
        
        for (String timeStamp: timeStamps) {
            Timestamp ts=Timestamp.valueOf(timeStamp);  
            Date login=new Date(ts.getTime());
            if (prevLogin != null) {
                long diff = diffInDays(login, prevLogin);
                if (diff > 1) {
                    consecutiveLogin = 1;
                } else if (diff == 1) {
                    consecutiveLogin++;
                }
                longestConsecutiveLogin = Math.max(longestConsecutiveLogin, consecutiveLogin);
            }
            prevLogin = login;
        }
        
        return longestConsecutiveLogin;
    }
    
    public static void main(String[] args) {
        String[] timeStamps = {"2021-03-13 15:13:05", "2021-03-13 23:13:05", "2021-03-16 15:13:05", "2021-03-16 23:13:05", "2021-03-17 07:13:05", "2021-03-17 15:13:05", "2021-03-17 23:13:05", "2021-03-18 07:13:05", "2021-03-18 15:13:05", "2021-03-22 15:13:05"};

        System.out.println(getLongestConsecutiveLogin(timeStamps));
    }
}