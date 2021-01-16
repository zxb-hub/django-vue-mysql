function signPwd() {
    pwd = document.getElementById('password').value
    if (pwd == '' || pwd == null) {
        pwd.placeholder = '密码不能为空';
        return false;
    }else{
        return true;
    }
}

function signPwdVerification() {
    pwd = document.getElementById('password').value
    pwds = document.getElementById('passwords').value
    if (pwds == '' || pwds == null) {
        pwds.placeholder = '确认密码不能为空';
        pwds.color = 'red';
        return false;
    } else if (pwds != pwd) {
        pwds.placeholder = '密码不同,请重新输入';
        pwds.color = 'red';
        return false;
    } else {
        return true;
    }
}