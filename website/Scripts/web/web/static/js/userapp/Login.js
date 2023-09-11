import ('./UUID.js')
let vue= new Vue({
    el:'#form',
    delimiters: [ '${','}'],
    data:{
        type:'',
        password:'',
        verify_code:'',


        error_message:[
            {type_error:'input right username, email or phone '},
            {password_error:'input right password'},
            {verify_code_error:'input Image verification code'}


        ],
        type_condition:false,
        password_condition:false,
        verify_code_condition:false,



    },
    methods:{
        check_verify_code: function (){
            if(!this.verify_code){
                this.verify_code_condition=true;
            }else{
                this.verify_code_condition=false;
            }
        },
        type_check:function () {
            if(!this.type){
               Vue.nextTick(function (){
                   vue.type_condition=true;
                   });

            }else{
               Vue.nextTick(function (){
                   vue.type_condition=false;
                   });


            }
        },
        password_check:function () {
            if(!this.password){
                Vue.nextTick(function (){
                    vue.password_condition=true;
                });
            }else{
                 Vue.nextTick(function (){
                    vue.password_condition=false;
                });
            }
        },
        Login_reg: function (){
            this.type_check();
            this.password_check();
            this.check_verify_code()
            if(this.password_condition || this.type_condition || this.verify_code_condition){
                window.event.returnValue=false;
            }
        }
    },
});




