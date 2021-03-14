getTaskPreviewList = async(token) => {
    let data = await request('/task-list', {}, token)
    return data
}

getDetailedtaskInfo = async(taskId) => {

}

createTask = async() => {
    
}

updateTask = async() => {

}

deleteDask = async() => {

}

login = async(uName, uPasswd) => {
    //return `Token ${await request(q, w, e, r)}`
}

logout = async() => {

}


request = async(url, params, token) => {
    return new Promise(resolve => {
        axios({
            headers: {
                Authorization: token
            },
            url: url,
            data: params
        })
        .then(response => {
            resolve(response.data)
        })    
        .catch(e => {
            resolve(false)
        })
    })
}