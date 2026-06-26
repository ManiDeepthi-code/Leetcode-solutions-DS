import streamlit as st

# 1. Your exact same math functions from before
def calculate_subtotal(food, delivery):
    return food + delivery

def apply_discount(subtotal_amt, coupon):
    return subtotal_amt - coupon

def split_bill(final_amt, friends):
    return final_amt / friends

# 2. Building the Web UI (User Interface)
st.set_page_config(page_title="Bill Splitter", page_icon="🍔")
st.title("🍔 Interactive Food Bill Splitter")
st.write("Adjust the inputs in the sidebar to calculate your shared bill instantly!")

st.markdown("---")

# 3. Creating interactive input boxes on the left sidebar
st.sidebar.header("📥 Enter Order Details")
food_total = st.sidebar.number_input("Food Items Total ($)", min_value=0, value=200, step=5)
delivery_charge = st.sidebar.number_input("Delivery Charge ($)", min_value=0, value=40, step=5)
discount_coupon = st.sidebar.number_input("Discount Coupon ($)", min_value=0, value=50, step=5)
split_between = st.sidebar.number_input("Split Between (People)", min_value=1, value=2, step=1)

# 4. Running your Python logic automatically behind the scenes
subtotal_amt = calculate_subtotal(food_total, delivery_charge)
discounted_total = apply_discount(subtotal_amt, discount_coupon)
each_person_owes = split_bill(discounted_total, split_between)

# 5. Displaying the results beautifully on the main screen
st.subheader("📊 Bill Breakdown")

# This splits the screen layout into 3 columns like a dashboard
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Subtotal (Food + Delivery)", value=f"${subtotal_amt}")
with col2:
    st.metric(label="Coupon Applied", value=f"-${discount_coupon}")
with col3:
    st.metric(label="Final Pool Total", value=f"${discounted_total}")

st.markdown("---")

# Display the final answer in a big green success box!
st.success(f"### 🎉 Each Friend Owes: **${each_person_owes:.2f}**")
