import streamlit as st
st.title("Grade calculator")
name=st.text_input("Enter your name")
index=st.text_input("Enter your index number")
Course_name=st.selectbox("Enter Course name:",["Biology","Chmistry","Maths","English","Physics",])
course_mark=st.number_input("Enter your course mark")
if st. button("Calculate grade"):
	
	course_mark= int(course_mark)/int(140)*100
	if course_mark <= 80:
	 	st.success("Grade A")
	elif course_mark <= 70:
	 	st.success("Grade B")
	elif course_mark <= 60:
	 	st.success("Grade C")
	elif course_mark <= 50:
		st.success("Grade D")
	elif course_mark < 50:
	   st. success("Fail")
course_name=course_mark
print(course_mark)

