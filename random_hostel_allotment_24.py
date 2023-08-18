#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import random
import numpy as np
from random import seed
from random import choice
from random import sample

def allocate_rooms(students, available_rooms):
    # Shuffle the student list to randomly allocate rooms
    random.shuffle(students)

    # Allocate rooms to students
    room_allocations = {}
    room_count = len(available_rooms)

    for i in range(0, len(students), 2):
        if room_count == 0:
            break
        
        student1 = students[i]
        student2 = students[i+1]
        room = available_rooms.pop(0)
        room_allocations[room] = [student1, student2]
        room_count -= 1
    
    return room_allocations

def main():
    st.title("Room Allocation App")
    st.subheader('Allotment of the Hostel Room at RLI-Kanpur for Students')
    st.subheader(':red[Method: Simple Random Sampling]')
    st.subheader(':blue[@Designed and Developed by Dr. Arkaprabha Sau,MBBS, MD (Gold Medalist), PhD (Research Scholar-Artificial Intelligence & Machine Learning)]')
    
    # Take input for available rooms and students list
    available_rooms_input = st.text_input("Enter available rooms (comma-separated)", "1,2,3,4,5,6,12,13,14,22,23,24,25,26,27")
    students_input = st.text_input("Enter student Roll Numbers applied for Hostel(comma-separated, Please Edit this list as per the roll number of the students applied for the hostel)", "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44")
    
    # Convert input strings to lists
    available_rooms = [int(room.strip()) for room in available_rooms_input.split(",")]
    students = [int(student.strip()) for student in students_input.split(",")]
    students = sample(students,24)
    

    if st.button("Allocate Rooms"):
        room_allocations = allocate_rooms(students, available_rooms)
        for room, students in room_allocations.items():
            st.write(f"Room {room}: {students[0]} and {students[1]}")

if __name__ == "__main__":
    main()


# In[ ]:




