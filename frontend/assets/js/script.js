    // This is the first and main function for the script, to validate all the fields//

    function validateForm(event) {
        event.preventDefault();

        // All variables are declared and linked to the HTML document //

        var firstname = document.getElementById("firstname");
        var firstnameError = document.getElementById("firstnameError");
        var lastname = document.getElementById("lastname");
        var lastnameError = document.getElementById("lastnameError");
        var email = document.getElementById("email");
        var emailError = document.getElementById("emailError");
    

        // If  field is left blank, the script writes directly to the HTML page prompting the user //

        if (firstname.value == "") {
            firstnameError.style.color = "red"
            firstnameError.innerHTML = "First Name required";
            firstname.focus();
            return false;
        }
        firstnameError.innerHTML = "";

        // If  field is left blank, the script writes directly to the HTML page prompting the user //

        if (lastname.value == "") {
            lastnameError.style.color = "red"
            lastnameError.innerHTML = "Lastname required";
            lastname.focus();
            return false;
        }
        lastnameError.innerHTML = "";

        // If  field is left blank, the script writes directly to the HTML page prompting the user //

        if (email.value == "") {
            emailError.style.color = "red"
            emailError.innerHTML = "Please Enter a Valid Email Address";
            email.focus();
            return false;
        }
        emailError.innerHTML = "";

        // If user does not use the '@' symbol when typing in their email it prompts the user to adjust //

        if (email.value.indexOf("@") == -1) {
            emailError.style.color = "red"
            emailError.innerHTML = "Please Enter a Valid Email Address";
            email.focus();
            return false;
        }
        emailError.innerHTML = "";

        // Final alert message to user that form has been filled in correctly //

        // alert("Thank you for your submission!");
        // return true;

            // Display submission message
    const submissionMessage = document.getElementById("submissionMessage");
    submissionMessage.style.display = "block";
    submissionMessage.innerHTML = "<p style='color:green;'>Thank you! Your form has been successfully submitted.</p>";

    // Optional: Reset the form fields
    document.forms["userForm"].reset();
    }

    // These next 2 functions style and highlight the fields on the HTML page when the user selects them //

    function changeBgd(textField) {
        textField.style.background = "lightyellow";
    }

    function resetBgd(textField) {
        textField.style.background = "lightgrey";
    }

    //This function is for the website switch statement with pop-up browser windows//

    function loadsites() {
        var choice = 0;
        choice = parseInt(prompt("Please Choose the website you would like to visit\n 1: Google\n 2: WWW3 Schools\n 3: TAFE SA", "1"));
        switch (choice) {
            case 1:
                window.open("https://www.google.com", "_blank", "toolbar=yes,menubar=yes scrollbars=yes,resizable=yes,top=30,left=30,width=800,height=800");
                break;

            case 2:
                window.open("https://www.w3schools.com", "_blank", "toolbar=yes,menubar=yes scrollbars=yes,resizable=yes,top=30,left=30,width=800,height=800");
                break;

            case 3:
                window.open("https://www.tafesa.edu.au", "_blank", "toolbar=yes,menubar=yes scrollbars=yes,resizable=yes,top=30,left=30,width=800,height=800");
                break;
        }
    }
