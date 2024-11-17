import streamlit as st
import random

mode = st.sidebar.radio("MODE", ["USER GUESSING", "COMPUTER GUESSING"])

if mode == "USER GUESSING":
    st.title("USER GUESSING")
    start = st.number_input("start_range", min_value=1, max_value=100)
    end = st.number_input("end_range", min_value=1, max_value=100)

    if start >=end:
        st.write("Starting range is greater than ending range")
    else:
        if "number_to_guess" not in st.session_state:
            st.session_state.number_to_guess = random.randint(start, end)
            st.session_state.attempt = 0
            

        st.title("GUESSING GAME")

        guess = st.number_input("Enter your guess", min_value=1, max_value=100)

        if st.button("START"):
            st.session_state.attempt += 1
            if guess < st.session_state.number_to_guess:
                st.write("It's too low, try again")
            elif guess > st.session_state.number_to_guess:
                st.write("It's too high, try again")
            else:
                st.write("Congratulations!! You found the number")
                
                st.balloons()
elif mode=="COMPUTER GUESSING":
    
    if "min_value" not in st.session_state:
        st.session_state.min_value=0
        st.session_state.max_value=100
        st.session_state.attempt=0
        st.session_state.computer_guess=(st.session_state.min_value+st.session_state.max_value)//2
        st.session_state.game_guess=False

    st.title("MACHINE GUESING")
    min_value=st.number_input("minium value is",value=1)
    max_value=st.number_input("maximum value is ",value=100)
    if st.button("START GAME"):
        if min_value > max_value:
            st.write("min_value is greater than max_value") 
        else:
            st.session_state.min_value=min_value
            st.session_state.max_value=max_value
            st.session_state.attempt=1
            st.session_state.computer_guess=(min_value+max_value)//2
            st.session_state.game_guess=True
            st.header(f"Machine guess is {st.session_state.computer_guess}")

    if st.session_state.game_guess:
           
        choice=st.radio("the machine guessing ?",["CORRECT","TOO LOW","TOO HIGH"])
        if st.button("sumbit"):
            if choice =="CORRECT":
                st.write(f"the machine guessing number is {st.session_state.computer_guess}")
                st.write(f"number of attempt {st.session_state.attempt}")
                st.balloons()
                st.session_state.game_guess=False
            else:

                if choice =="TOO LOW":
                    st.session_state.min_value=st.session_state.computer_guess+1
                    st.write("machine guess is low")
                elif choice =="TOO HIGH":
                    st.session_state.max_value=st.session_state.computer_guess-1
                    st.write("the machine guess is high")          

                
                st.session_state.computer_guess=(st.session_state.min_value+st.session_state.max_value)//2
                st.session_state.attempt+=1
                st.header(f"The machine's new guess is {st.session_state.computer_guess}")


        