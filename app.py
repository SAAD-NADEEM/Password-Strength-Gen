import streamlit as st
import string

def check_password_strength(password):
    strength = 0
    remarks = []

    # Check length
    if len(password) >= 12:
        strength += 1
    elif len(password) >= 8:
        remarks.append("🟡 Password is a bit short. Consider using at least 12 characters.")
    else:
        remarks.append("🔴 Password is too short. Use at least 8 characters.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        remarks.append("🟡 Consider adding uppercase letters for better security.")

    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        remarks.append("🟡 Consider adding numbers for better security.")

    # Check for special characters
    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        remarks.append("🟡 Consider adding special characters (e.g., !, @, #) for better security.")

    # Evaluate strength
    if strength == 4:
        remarks.append("🟢 Your password is very strong! Great job! 💪")
    elif strength == 3:
        remarks.append("🟢 Your password is strong, but it could be improved. 👍")
    elif strength == 2:
        remarks.append("🟠 Your password is moderate. Consider improving it. 🤔")
    elif strength == 1:
        remarks.append("🔴 Your password is weak. You should improve it. 🚨")
    else:
        remarks.append("🔴 Your password is very weak. Please make it stronger. ⚠️")

    return strength, remarks

def main():
    # Add a fun header with emojis
    st.title("🔐 Password Strength Checker")
    st.write("Check how strong your password is and get tips to improve it! 💡")

    # Input field for password
    password = st.text_input("Enter your password to check its strength:", type="password")

    if password:
        # Check password strength
        strength, remarks = check_password_strength(password)

        # Display strength level with emojis
        st.write(f"**Password Strength Level:** {strength}/4 {get_strength_emoji(strength)}")

        # Display remarks with emojis
        st.write("**Remarks:**")
        for remark in remarks:
            st.write(remark)

def get_strength_emoji(strength):
    # Return an emoji based on strength level
    if strength == 4:
        return "💪🟢"  # Very strong
    elif strength == 3:
        return "👍🟢"  # Strong
    elif strength == 2:
        return "🤔🟠"  # Moderate
    elif strength == 1:
        return "🚨🔴"  # Weak
    else:
        return "⚠️🔴"  # Very weak

if __name__ == "__main__":
    main()