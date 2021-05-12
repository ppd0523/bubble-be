function strfdate(date){
    let year = date.getFullYear()
    let month = (1 + date.getMonth())
    month = month >= 10 ? month : '0' + month
    let day = date.getDate()
    day = day >= 10 ? day : '0' + day
    return year + '-' + month + '-' + day
}

// console.log(strfdate(new Date("2021-05-02")))