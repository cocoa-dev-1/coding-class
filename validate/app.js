const form = document.getElementById('form');
const error = document.getElementById('error');

function checkValidate(){
    error.style.display = 'none';
    error.innerHTML = '';
    
    if (!checkEmail(form.email.value)){
        return false
    } else if (!checkPassword(form.password.value, form.password2.value)){
        return false
    }
    return true
}
function checkIsVailed(val, text){
    if (val == ''){
        error.innerHTML = text;
        error.style.display = 'block';
        return false
    }
    return true
}

function checkEmail(email){
    const emailRegExp = /^[A-Za-z0-9_]+[A-Za-z0-9]*[@]{1}[A-Za-z0-9]+[A-Za-z0-9]*[.]{1}[A-Za-z]{2,}$/;
    if (!checkIsVailed(email, 'email을 적어주세요.')){
        form.email.focus();
        return false
    }
    if (!emailRegExp.test(email)){
        error.innerHTML = 'email이 올바르지 않습니다.'
        error.style.display = 'block';
        form.email.focus();
        return false
    }
    return true
}

function checkPassword(pwd, pwd2){
    const pwdRegExp = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}/;
    if (!checkIsVailed(pwd, '비밀번호를 입력해 주세요.')){
        form.password.focus();
        return false
    }

    if (!checkIsVailed(pwd2, '비밀번호 확인란을 입력해주세요.')){
        form.password2.focus();
        return false
    }

    if (!pwdRegExp.test(pwd) || !(pwd.length < 20)){
        error.innerHTML = '비밀번호가 올바르지 않습니다.';
        error.style.display = 'block';
        form.password.focus();
        return false
    }

    if (!(pwd === pwd2)){
        error.innerHTML = '비밀번호와 비밀번호 확인란이 일치 하지 않습니다.';
        error.style.display = 'block';
        form.password2.focus();
        return false
    }
    return true
}