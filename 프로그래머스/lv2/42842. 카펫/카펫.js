function solution(brown, yellow) {
    for(let width=1;;width++){
        for(let height=1;height<=width; height++){
            if(height*width == brown+yellow && (width-2)*(height-2)==yellow){
                return [width, height]
            }
        }
    }
}