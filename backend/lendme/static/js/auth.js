const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const openPopUp = document.getElementById('open-pop-up');
const closePopUp = document.getElementById('pop-up-close')
const popUp = document.getElementById('pop-up')

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

openPopUp.addEventListener('click', function(e)  {
    e.preventDefault();
    popUp.classList.add('active');

});

closePopUp.addEventListener('click', () => {
    popUp.classList.remove('active');
    window.location.href = "/";
});
