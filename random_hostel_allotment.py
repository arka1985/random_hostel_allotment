#!/usr/bin/env python
# coding: utf-8

# In[6]:


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
    
    # Take input for available rooms and students list
    available_rooms_input = st.text_input("Enter available rooms (comma-separated)", "1,2,3,4,5,6,12,13,14,22,23,24,25,26,27")
    students_input = st.text_input("Enter student Roll Numbers applied for Hostel", "5, 8, 44, 31, 35, 43, 41, 34, 29, 12, 11, 26, 9, 37, 3, 24, 38, 17, 16, 14, 33, 10, 18, 7, 2, 13, 39, 21, 4, 46, 20")
    
    # Convert input strings to lists
    available_rooms = [int(room.strip()) for room in available_rooms_input.split(",")]
    students = [int(student.strip()) for student in students_input.split(",")]
    students = sample(students, 30)
    

    if st.button("Allocate Rooms"):
        room_allocations = allocate_rooms(students, available_rooms)
        for room, students in room_allocations.items():
            st.write(f"Room {room}: {students[0]} and {students[1]}")

if __name__ == "__main__":
    main()


# In[ ]:




