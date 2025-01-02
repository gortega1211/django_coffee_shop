document.addEventListener('DOMContentLoaded', function () {
    var navbarToggler = document.querySelector('.navbar-toggler');
    var btnMyOrder = document.getElementById('btn-my-order');
    var btnLogout = document.getElementById('btn-logout');
    var btnSignUp = document.getElementById('btn-signup');
    var btnLogin = document.getElementById('btn-login');
    var nvlMyOrder = document.getElementById('nvl-my-order');
    var nvlLogout = document.getElementById('nvl-logout');
    var nvlSignUp = document.getElementById('nvl-signup');
    var nvlLogin = document.getElementById('nvl-login');

    function addClassHidden(items) {
        items.forEach(function (item) {
            if (item != null) {
                item.classList.add("visually-hidden");
            }
        });
    }

    function removeClassHidden(items) {
        items.forEach(function (item) {
            if (item != null) {
                item.classList.remove("visually-hidden");
            }
        });
    }

    function checkNavbarTogglerVisibility() {
        if (navbarToggler.offsetParent !== null) {
            addClassHidden([btnMyOrder, btnLogout, btnSignUp, btnLogin]);
            removeClassHidden([nvlMyOrder, nvlLogout, nvlSignUp, nvlLogin]);
        } else {
            removeClassHidden([btnMyOrder, btnLogout, btnSignUp, btnLogin]);
            addClassHidden([nvlMyOrder, nvlLogout, nvlSignUp, nvlLogin]);
        }
    }

    checkNavbarTogglerVisibility();

    window.addEventListener('resize', checkNavbarTogglerVisibility);
});