function solution(arr)
{
    let res = [];
    let current = arr[0];
    res.push(arr[0]);
    
    for(let i = 1; i < arr.length; i++){
        if(current === arr[i]){
            continue;
        }
        else{
            res.push(arr[i]);
            current = arr[i];
        }
    }
    
    return res;
}