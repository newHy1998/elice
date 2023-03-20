function solution(food) {
    let res = [0];
    let foodNumber = food.length - 1;
    for(var i = food.length - 1; i > 0; i--){
        if(Number(food[i]) % 2 == 0){
                idx = Number(food[i]) / 2;
                 for(let i = 0; i < idx; i++){
                     res.push(foodNumber);
                     res.unshift(foodNumber);
                 }
            }
            else{
                idx = (Number(food[i]) - 1) / 2;
                for(let i = 0; i < idx; i++){
                     res.push(foodNumber);
                     res.unshift(foodNumber);
                 }
            }
        foodNumber -= 1;
        
    }
    
    res = res.join("");
    
    return res;
}