#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import random

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
    
    students = [
        'Student1', 'Student2', 'Student3', 'Student4', 'Student5',
        'Student6', 'Student7', 'Student8', 'Student9', 'Student10',
        'Student11', 'Student12', 'Student13', 'Student14', 'Student15',
        'Student16', 'Student17', 'Student18', 'Student19', 'Student20',
        'Student21', 'Student22', 'Student23', 'Student24', 'Student25',
        'Student26', 'Student27', 'Student28', 'Student29', 'Student30'
    ]

    available_rooms = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 201, 202, 203, 204, 205]
    
    if st.button("Allocate Rooms"):
        room_allocations = allocate_rooms(students, available_rooms)
        for room, students in room_allocations.items():
            st.write(f"Room {room}: {students[0]} and {students[1]}")

if __name__ == "__main__":
    main()


# In[2]:


streamlit run room_allocation_app.py


# In[ ]:




