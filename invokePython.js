function invokePython(clientEmail){
const spawn = require('child_process').spawn;
const process = spawn('python3', ['matchingAlgo.py', clientEmail]);
var retur;
process.stdout.on('data', data => {
    
    retur = (' ' + data.toString()).slice(1);
    
});


return retur;
}
exports.invokePython = invokePython;

