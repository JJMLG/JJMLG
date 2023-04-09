const calc=(ny, nm, nd, termMonth) =>{
    nd-=1;
    if(!nd){
        nd=28;
        nm--;
    }
    nm+=termMonth;
    if (nm>12){
        ny+=Math.floor((nm-1)/12);
        nm%=12;
        if(nm==0) nm=12;
    }
    return [ny,nm, nd];
}
function solution(today, terms, privacies) {
    let [ny, nm, nd] = today.split(".");
    ny = +ny;
    nm = +nm;
    nd = +nd;
    
    const privList = privacies.map(el=>{
        const py = el.slice(0,4);
        const pm = el.slice(5,7);
        const pd = el.slice(8,10);
        const dd = el.slice(11);
        return [py, pm,pd,dd];
    })
    let fromToday={};

    const termList = terms.map(el=>{
        let [cond, termMonth] = el.split(" ");    
        termMonth = +termMonth;
        fromToday[cond] = termMonth;
    })
    let answer = privList.reduce((init,el,idx)=>{
        const [py, pm,pd,termC] = el;
        const res = calc(+py, +pm, +pd, fromToday[termC]);
        if(res[0]>ny) return init;
        else if(res[0]<ny){
            return [...init,idx+1];
        }else{
            if(res[1]>nm) return init;
            else if (res[1]<nm) return [...init,idx+1];
            else{
                if(res[2]>=nd) return init;
                return [...init,idx+1];
            }
        }
    },[]);
    return answer;
}