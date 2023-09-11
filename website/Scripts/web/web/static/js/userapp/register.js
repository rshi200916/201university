import("../query.js")
let vue=new Vue({
			el:'#mod',
            delimiters:[ '${','}'],
			data:{
				error_message:[
					{error_phone:'input right phone, like 3344921353'},
					{error_email:'input right email'},
					{error_password:' have uppercase letter, lowercase letter, number, Length 8-16'},
					{error_comfirm:'can not match'},
					{error_last_name:'can not be null'},
					{error_first_name:'can not be null'},
					{error_recheck_username:"username='last name - firstname', this username has registered"},
					{error_recheck_phone:"this phone has registered"},



					],
			first_name:'',
			last_name:'',
			phone:'',
			email:'',
			password:'',
			comfirm:'',
			phone_condition:false,
			email_condition:false,
			password_condition:false,
			comfirm_condition:false,
			first_name_condition:false,
			last_name_condition:false,
			recheck_username_condition: false,
			recheck_phone_condition:false,





							},
		    methods: {

				check_last_name:function(){
					if(!this.last_name){
						this.last_name_condition=true;
					}else{
						this.last_name_condition=false;
					}

				},
				check_first_name:function(){
					if(!this.first_name){
						this.first_name_condition=true;
						console.log(this.first_name_condition)
					}else{
						this.first_name_condition=false;
					}
					if( !this.first_name_condition && !this.last_name_condition){
						let username=this.last_name + "-" + this.first_name;
						$.get("/username/"+username+"/count/",function (data){
							if(data.count==1){
								Vue.nextTick(function (){
									vue.recheck_username_condition=true;
								});
							}else{
									Vue.nextTick(function (){
									vue.recheck_username_condition=false;
								});
							}



						});

					}


				},
			check_phone: function(){
					let str =/[2-9][0-9]{2}[2-9][0-9]{2}[0-9]{4}/;
					if(!str.test(this.phone)){
						this.phone_condition=true;
					}else{
						this.phone_condition=false;
					}
					if(!this.phone_condition){
						$.get("/phone/"+this.phone+"/count/",function (data){
						if(data.count==1){
							Vue.nextTick(function(){
								vue.recheck_phone_condition=true;
							});
						}else{
							Vue.nextTick(function(){
								vue.recheck_phone_condition=false;
							});
						}

					});
					}


				},
				check_email:function(){
					let str=/^([0-9a-zA-Z_-])+@([a-zA-Z0-p_-])+(.[a-zA-Z0-9_-])+/;
					if(!str.test(this.email)){
						this.email_condition=true;
					}else{
						this.email_condition=false;
					}
				},
				check_password:function(){
					// let str=/\w{1,}/
					let str=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/;

					if(!str.test(this.password)){
						this.password_condition=true;
					}else{
						this.password_condition=false;
					}

				},
				check_comfirm:function(){
					if(this.comfirm==this.password){
						this.comfirm_condition=false;
					}else{
						this.comfirm_condition=true;
					}
				},
				reg_submit:function (){
				this.check_email()
				this.check_comfirm();
				this.check_password();
				this.check_comfirm();
				this.check_phone();
				this.check_first_name();
				this.check_last_name();
				if(this.phone_condition|| this.email_condition|| this.password_condition || this.comfirm_condition){
					window.event.returnValue=false;
				}


				},
		    },


		});



