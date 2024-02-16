// Добавление возможности пользователю просматривать пароль, который он вводит

document.addEventListener("DOMContentLoaded", function() {
    const showPasswordIcons = document.querySelectorAll(".show-password-icon");

    showPasswordIcons.forEach(icon => {
        icon.addEventListener("click", function() {
            const inputField = this.previousElementSibling;
            if (inputField.type === "password") {
                inputField.type = "text";
            } else {
                inputField.type = "password";
            }
        });
    });
});
