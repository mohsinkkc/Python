class Country:

     def ShowCountry(self):

         print("You are now in India");

class State(Country):

     def ShowState(self):

         print("You are in Ahmedabad");

st =State();

st.ShowCountry();

st.ShowState();
