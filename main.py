# This project is where you show off your ability to (1) translate a business requirement into a database design, (2) design a database using one-to-many and many-to-many relationships, and (3) know when to use LEFT and/or RIGHT JOINs to build result sets for reportingAn organization grants key-card access to rooms based on groups that key-card holders belong to. You may assume that users below to only one group. Your job is to design the database that supports the key-card system.
There are six users, and four groups. Modesto and Ayine are in group “I.T.” Christopher and Cheong woo are in group “Sales”. There are four rooms: “101”, “102”, “Auditorium A”, and “Auditorium B”. Saulat is in group “Administration.” Group “Operations” currently doesn’t have any users assigned. I.T. should be able to access Rooms 101 and 102. Sales should be able to access Rooms 102 and Auditorium A. Administration does not have access to any rooms. Heidy is a new employee, who has not yet been assigned to any group.
After you determine the tables any relationships between the tables (One to many? Many to one? Many to many?), you should create the tables and populate them with the information indicated above.





DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Groupss;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS UsersGroups;
DROP TABLE IF EXISTS GroupsRooms;
DROP TABLE IF EXISTS UsersGroupsRooms;
CREATE TABLE Users ( UserId int PRIMARY KEY, UserName varchar (30) Not NULL);
INSERT INTO Users ( UserId, UserName ) VALUES (1, 'Modesto');
INSERT INTO Users ( UserId, UserName ) VALUES (2, 'Ayine');
INSERT INTO Users ( UserId, UserName ) VALUES (3, 'Christopher');
INSERT INTO Users ( UserId, UserName ) VALUES (4, 'Cheong');
INSERT INTO Users ( UserId, UserName ) VALUES (5, 'Saulat');
INSERT INTO Users ( UserId, UserName ) VALUES (6, 'Heidy');
SELECT * FROM Users;
CREATE TABLE Rooms ( RoomId int PRIMARY KEY, RoomName varchar (30) NOT NULL );
INSERT INTO Rooms ( RoomId, RoomName ) VALUES ( 101,'101');
INSERT INTO Rooms ( RoomId, RoomName ) VALUES ( 102,'102');
INSERT INTO Rooms ( RoomId, RoomName ) VALUES ( 103,'Auditorium A');
INSERT INTO Rooms ( RoomId, RoomName ) VALUES ( 104,'Auditorium B');
SELECT * FROM Rooms;
CREATE TABLE UsersGroups( UgId int PRIMARY KEY, UserId int NOT NULL, GrampId int NOT NULL );
INSERT INTO UsersGroups ( UgId, UserId, GroupId ) VALUES ( 121, 1, 21) ;
INSERT INTO UsersGroups ( UgId, UserId, GroupId ) VALUES ( 122, 2, 21) ;
INSERT INTO UsersGroups ( UgId, UserId, GroupId ) VALUES ( 123, 3, 22) ;
INSERT INTO UsersGroups ( UgId, UserId, GroupId ) VALUES ( 124, 4, 22) ;
SELECT * FROM UsersGroups;
CREATE TABLE GroupsRooms ( GrId int PRIMARY KEY, GroupId int NOT NULL, RoomId int NOT NULL );
INSERT INTO GroupsRooms ( GrId, GroupId, RoomId ) VALUES ( 1101, 21, 101) ;
INSERT INTO GroupsRooms ( GrId, GroupId, RoomId ) VALUES ( 1102, 21, 102) ;
INSERT INTO GroupsRooms ( GrId, GroupId, RoomId ) VALUES ( 1103, 22, 102) ;
INSERT INTO GroupsRooms ( GrId, GroupId, RoomId ) VALUES ( 1104, 22, 103) ;
SELECT * FROM GroupsRomms;
CREATE TABLE GroupsRooms ( UgrId int PRIMARY KEY, GroupId int NOT NULL,
RoomId int NOT NULL );
INSERT INTO UsersGroupsRooms ( UgrId, UserId, GroupId, RoomId ) VALUES ( 2101, 1, 21, 101) ;
INSERT INTO UsersGroupsRooms ( UgrId, UserId, GroupId, RoomId ) VALUES ( 2102, 2, 21, 102) ;
INSERT INTO UsersGroupsRooms ( UgrId, UserId, GroupId, RoomId ) VALUES ( 2103, 3, 22, 102 );
INSERT INTO UsersGroupsRooms ( UgrId, UserId, GroupId, RoomId ) VALUES ( 2104, 4, 22, 103) ;


--------
Next, write SELECT statements that provide the following information:
• All groups, and the users in each group. A group should appear even if there are no users assigned to the group.
• All rooms, and the groups assigned to each room. The rooms should appear even if no groups have been
assigned to them.
• A list of users, the groups that they belong to, and the rooms to which they are assigned. This should be sorted
alphabetically by user, then by group, then by room.

MySQLSelect =
 “ SELECT .GroupName, u. UserName FROM Users u INNER JOIN UsersGroups ug
ON u. UserId = ug. UserId RIGHT JOIN Groupss g
ON ug.GroupId = g.GroupId;
SELECT r.RoomName, g.GroupName FROM Groupss g INNER JOIN GroupsRooms
ON g. GroupId
= gr.GroupId RIGHT JOIN Rooms r
ON gr. RoomId = r.RoomId;
SELECT u.UserName, g.GroupName, r.RoomName
FROM Users
u INNER JOIN UsersGroupsRooms ugr
ON u.UserId =
ugr. UserId INNER JOIN Groupss
ON ugr. GroupId
= g. GroupId INNER JOIN Rooms
r
ON ugr.RoomId = r.RoomId
ORDER BY UserName, GroupName, RoomName; “

