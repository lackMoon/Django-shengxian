$(function(){
    var login_name;
    var login_pwd;
    var error_name=false;
    var error_pwd=false;
    $('.name_input').blur(function(){
        check_login_name();
    });
    $('.pass_input').blur(function(){
        check_login_pwd();
    });
    function check_login_name(){
        login_name=$('.name_input').val();
        $.get("/user/user_exist/?uname="+login_name,function(data){
            if (data.exist==true){
                $('.user_error').hide();
                error_name=false;
            }
            else {
                $('.user_error').html("此用户不存在").show();
                error_name=true;
            }
        });
    }
    function check_login_pwd(){
        login_pwd=$('.pass_input').val();
        $.get("/user/login_varify/?uname="+login_name+"&upwd="+login_pwd,function(data){
            if(data.varify==true){
                $('.pwd_error').hide();
                error_pwd=false;
            }
            else{
                $('.pwd_error').html("密码错误").show();
                error_pwd=true;
            }
        });
    }


    $('.form_input').submit(function(){
        check_login_name();
        check_login_pwd();
        if(error_name==false&&error_pwd==false){
            return true;
        }
        else{
            alert("用户名或密码错误");
            return false;
        }
    });






})