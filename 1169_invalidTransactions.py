class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        processedTransactions = [transaction.split(',') for transaction in transactions]
        invalidTransactions = set()
        for i, transaction in enumerate(processedTransactions):
            name, time, amount, city = transaction
            time, amount = int(time), int(amount)
            if amount > 1000:
                invalidTransactions.add(i)
                continue
            
            for j, otherTransaction in enumerate(processedTransactions):
                otherName, otherTime, _, otherCity = otherTransaction
                otherTime = int(otherTime)
                if(
                    i != j 
                    and name == otherName 
                    and abs(time - otherTime) <= 60
                    and city != otherCity
                ):
                    invalidTransactions.add(j)
                    invalidTransactions.add(i)
                    break
        
        output = []
        for idx in invalidTransactions:
            output.append(transactions[idx])
        return output
