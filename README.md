# Student-Teacher-Portal
The primary goal of this project is to design an intuitive application for file management and lecture scheduling, akin to the functionality provided by Nucleus. This application is tailored to assist faculty and students within an educational institution. Faculty members can input their lecture timings to generate an optimal schedule or upload files for students' reference. On the other hand, students can log in to access uploaded files or view a specific faculty member's schedule.

Key features include:

Unique Login IDs and Passwords: Each user, whether faculty or student, has a distinct login ID and password. A separate file tracks their previously uploaded file details, simplifying access based on user needs.

Optimal Schedule Generation: Utilizing interval trees, each representing a lecture hall, ensures there are no scheduling conflicts between faculty members. The faculty ID is stored within the interval tree entry, enabling searches for a particular faculty member's lectures to be uploaded into their respective schedule files.

Data structures employed:

File Management System: B Trees are utilized to create an efficient file management system.
Login Activity Management: AVL Trees are used to manage login activities and user authentication.
Optimal Lecture Schedule Generation: Interval Trees are employed to generate an optimal lecture schedule, ensuring no overlaps in lecture timings within lecture halls.
How the program operates:

Upon launching, the program prompts users for their login ID and password.
Students, upon login, can search for and view uploaded files.
Faculty members, upon login, have options to:
Upload files or view previously uploaded files.
Receive an optimal schedule based on provided timings, ensuring minimal scheduling conflicts.
This application streamlines file management and lecture scheduling processes, providing a user-friendly interface for faculty and students within the educational institution.
