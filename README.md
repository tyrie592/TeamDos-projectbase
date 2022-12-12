# TreasureChest

![WhatsApp Image 2022-11-29 at 5 33 02 PM](https://user-images.githubusercontent.com/46247477/204969588-af16b278-c76c-49a7-a750-a71515e42f6c.jpeg)

## Purpose
TreasureChest is an inventory management software written in python, created by TeamDos of CEN4010 for the semester scrumm project.

---

#### Function Summary

This software aims to help a user manage their store inventory of books and shoes, and includes a number of features:
- Sort and organize inventory by price, brand, or popularity
- View and sort shoes or books list independently
- Track and archive market prices of items
- Track inventory availibilty
- Import and save inventory lists in the form of CSV files
- Modify and export CSV files
- Upload data using Google Sheets API
- Nice and usable GUI (maybe)



#### Nerd Stuff
This software has been completely written in python, and intakes data in the form of CSV files. These files are processed using the Google Sheets API, and then can be saved locally or on an external server, depending on the user's discretion. These sheets can then be displayed throught the GUI, made in PythonQT. An example of this GUI is shown below, demostrating 2 sheets that can be viewed.

![image](https://user-images.githubusercontent.com/46247477/206955461-76119a06-a86d-479e-b14d-17e34636e765.png)

Once completely installed, this program contains 3 main folders. One contains the code itself, including InstallAssist and the TreasureChest program itself; the second contains documentation, such as meeting minutes written during Zoom standup meetings, psuedocode, backlog grooming sheets, and more. The final folder contains documents requested by the professor. These folders are displayed below.

![Screenshot 2022-12-11 at 9 32 20 PM](https://user-images.githubusercontent.com/46247477/206955578-95ba7b03-b116-4ec5-a078-eaa564040cc8.png)

This program is capable of running on any machine/os equipped with Python, although the installation guide is MacOs-specific.



#### Getting Started (MacOs Specific)
The software files may be delivered via a public webpage which requires credentials, or in the form of a drive.

After downloading the zip, extra python packages must be downloaded first before the program itself can run. To do this, locate the cog gear icon ![image](https://user-images.githubusercontent.com/46247477/206955647-35e2c91c-1044-4e3b-a863-ec9a0bd76f96.png)
in the folder and double click. This will download all packages neccesary to run the program to your pc. 

Before going further, you should ensure Homebrew is installed to your mac and is up to date.

Once this is finished, the user must define where to store the data and application. There are two main options: pushing data to a private cloud, or storing data ocally where the app runs. If you plan on storing locally, you will need SQL. The tutorial in the user manual uses MariaDB, but there are other options. Once MariaDB is installed, it must be started to test log in. Once this is complete, you can move on to uploading sheets.

> **Note:** This is a very basic summary. For further installation instructions and program details, please refer to pages 4-6 of the user manual, linked below.


[TreasureChest-WRD.pdf](https://github.com/tyrie592/TeamDos-projectbase/files/10204440/TreasureChest-WRD.pdf)



#### Uploading Sheets

Once installed, the program (located in the code folder) should look like the image below.

![image](https://user-images.githubusercontent.com/46247477/206957506-3cc1b614-c055-4f6b-ab3c-55a851d5ae67.png)

The treasure chest icon will start the program locally. If the JSON file does not match you to an available Google instance, then either you or we probably messed up somewhere and you should either open a issue or try to fix it yourself (tentatively recommended). Once launched successfully, it will display the individual inventories requested during the initial setup. Your local databases can be used to perform queries and updates to the sheets avaliable.


