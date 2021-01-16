function changeLogin(){
    
    loginSpan=document.getElementById('loginSpan')
    signinSpan=document.getElementById('signinSpan')
    login=document.getElementById('login')
    signin=document.getElementById('signin')

    login.className='loginAction';
    signin.className='signinOff';
    loginSpan.className='loginSpanChange';
    signinSpan.className='signinSpan';
}
function changeSignin(){
    login=document.getElementById('login')
    signin=document.getElementById('signin')
    loginSpan=document.getElementById('loginSpan')
    signinSpan=document.getElementById('signinSpan')
    
    login.className='loginOff';
    signin.className='signinAction';
    signinSpan.className='signinSpanChange';
    loginSpan.className='loginSpan';

}