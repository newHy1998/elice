function solution(progresses, speeds) {
    let res = [];
    let number = 0;
    
    while(0 < progresses.length){
        for(let i = 0; i < progresses.length; i++){
            progresses[i] += speeds[i];
        }
        
        while(true){
            if(progresses[0] >= 100){
                number += 1;
                progresses.shift();
                speeds.shift();
            }
            else{
                if(number > 0){
                    res.push(number);
                    number = 0;
                }
                break;
            }
        }
    }
    
    return res;
}