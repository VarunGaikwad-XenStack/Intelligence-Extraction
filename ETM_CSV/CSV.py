import csv
import pandas as pd


class csv():
        
        def uOpen():
                a= input('Enter the name of your input file: ')
                global y
                y= input("Enter the name of column to split: ")
            
                with open(a,'r') as csv_file:
                    csv_reader= csv.DictReader(csv_file)
                
                    for line in csv_reader:
                        global b
                        b=input('Enter new name of csv File: ') 
                        with open(b,'w') as new_file:
                          csv_writer = csv.writer(new_file, delimiter='\t')
                          for line in csv_reader:
                              
                           #csv_writer.writerow(line[y].split('/'))
                              csv_writer.writerow(line[y])


               
        def split():
            r=pd.read_csv(b,error_bad_lines=False)
            r.columns=[y]
            r.dropna(inplace=True)
            new = r[y].str.split("/", n = 4, expand = True) 
            r[1]=new[0]
            r[2]=new[1]
            r[3]=new[2]
            r[4]=new[3]
            r[5]=new[4]
            r.drop(columns =[y], inplace = True) 
            new= new.fillna(0)
            c=input('Enter the Output file name:')
            new.to_csv(c)
                
                
            
            
          

