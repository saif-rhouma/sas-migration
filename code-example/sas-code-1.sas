/* Assign library */
LIBNAME mylib "/home/user/sasdata";

/* Read Excel file */
LIBNAME xldata XLSX "/home/user/files/sales.xlsx";

/* Create table from Excel sheet */
DATA mylib.sales_data;
    SET xldata.'Sheet1$'n;
RUN;

/* SQL Processing */
PROC SQL;
    CREATE TABLE mylib.high_sales AS
    SELECT id, amount
    FROM mylib.sales_data
    WHERE amount > 1000;
QUIT;

/* Export to CSV */
DATA _NULL_;
    SET mylib.high_sales;
    FILE "/home/user/output/high_sales.csv";
    PUT id amount;
RUN;