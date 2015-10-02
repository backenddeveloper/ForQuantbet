/*
 * Copyright Graham Turner 2015. Released for use under the GNU/GPLv3. This code is not suitable for production use.
 *
 * To Run copy and paste this file into the browser console while on the quantbet.com website.
 */

; function get(callback , xhttp){

    xhttp.open("GET" , "/quiz" , false) ;
    xhttp.onreadystatechange = function(){
        if(xhttp.readyState === 4 && xhttp.status === 200){
            callback(xhttp.response) ;
        }
    }
    xhttp.send() ;

}

function parse(string , callback){
    
    try {
        
        var numbers = [                        
            parseInt(string.split('<strong>')[1].split('</strong>')[0]),
            parseInt(string.split('<strong>')[2].split('</strong>')[0])
        ]
        
        callback(numbers) ;
        
    } catch (err){
     
        console.log("A parse error occured.") ;
        throw err ;
        
    }    
    
}

function getGCD(numbers , callback){
 
    try {
        
        var gcdFinder = function(a, b) {
            if ( ! b) {
                return a;
            }

            return gcdFinder(b, a % b);
        };                
        
        var _gcd = gcdFinder(numbers[0] , numbers[1]) ;
        
        callback(_gcd) ;
        
    } catch (err){
        
        console.log("An error occured finding the GCD") ;
        throw err ;
        
    }
    
}

function post(divisor , callback , xhttp){

    xhttp.open("POST" , "/submit" , false) ;
    xhttp.setRequestHeader("Content-Type" , "application/x-www-form-urlencoded") ;
    xhttp.onreadystatechange = function(){
        if(xhttp.readyState === 4 && xhttp.status === 200){
            callback(xhttp.response) ;
        }
    }
    xhttp.send("divisor=" + divisor.toString()) ;

}

(function(){
    
    get(function(string){
        parse(string , function(numbers){
            getGCD(numbers , function(divisor){
                post(divisor , function(reply){
                    console.log(reply) ;
                } , new XMLHttpRequest());
            });
        });
    } , new XMLHttpRequest());
    
})();
