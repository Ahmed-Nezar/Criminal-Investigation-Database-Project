# Database-Project

## Note:
To work with the database correctly & push it to github you need to follow the following steps:
1. Open Sql Server Management Studio (SSMS)
2. Connect to the server
3. Right click on the database you want to push to github
4. Click on "Tasks" -> "Export Data-tier Application"
5. Click
6. Choose the path where you want to save the file & name it with the following name: "Criminal Investigation System"
7. Click "Next"
8. Click "Finish"

Now you have the database file in your local machine, you can push it to github.

To work with the database correctly & pull it from github you need to follow the following steps:
1. Open Sql Server Management Studio (SSMS)
2. Connect to the server
3. Delete old version of Criminal Investigation System if exists (Right click on the database -> Delete)
4. Right click on the Databases Folder
5. Click on "Import Data-tier Application"
6. Click "Next"
7. Choose the path of the file you want to import
8. Click "Next"
9. Click "Finish"

For reference check this [link.](https://www.youtube.com/watch?v=XLzV_gagkZc)

## For GUI:
1. Open the project in Visual Studio Code
2. Open the terminal
3. Run the following command:
```bash
 cd GUI/Tkinter-Designer
 pip install -r requirements.txt
```
4. Create Figma account to create the GUI design
5. Run gui.py in the Tiknter-Designer folder to generate the GUI code
6. Create a token in the Figma account
7. Copy the token and paste it
8. Copy Desgin URL and paste it

### Naming is Important in Figma

| Figma Element Name | Tkinter Element |
| --- | --- |
| Button | Button |
| Line | Line |
| Text | Name it anything |
| Rectangle | Rectangle |
| TextArea | Text Area |
| TextBox | Entry |
| Image | Canvas.Image() |
| ButtonHover (EXPERIMENTAL) | Button shown on hover |

For reference check this [link.](https://www.youtube.com/watch?v=oLxFqpUbaAE)

