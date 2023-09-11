import("../query.js")
import('../vue.js')
let vue = new Vue({
				el:'#mod',
                delimiters:[ '${','}'],
				data:{
					error_message:[
						{error_price:'please input correct number'},
					],
					price:'',
					price_condition: false,

				},
				methods:{
					check_price:function(){
						let str = /^[0-9]+(.[0-9]{1,4})$|(^[1-9][0-9]*$)/;
						if(!this.price){
							Vue.nextTick(function (){
									vue.price_condition=true;
								});
						}else if(!str.test(this.price)){
								Vue.nextTick(function (){
									vue.price_condition=true;
								});
						}else{
								Vue.nextTick(function (){
									vue.price_condition=false;
								});
						}
					},
					reg_submit:function(){
						this.check_price()
						if(!this.price_condition){
							window.event.returnValue=false;
						}
					}
				}


			});