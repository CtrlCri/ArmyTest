/** ToDo */
class BinaryParser {
    /**
     * ToDo
     * v0.1.0 | [ArmyCrih] | First version
     * 
     * @param {buffer} buffer -> Trama a deserializar
     * @param {*} format -> Formato de serialización 
     * @return {*} Objeto "composicion" (trama deserializada en campos tag = valor)
     * 
     */
    decode(buffer, format) {
        let _object = {}
        //ToDo
        return _object;
    }

    /**
     * 
     * @param {*} _object -> Objeto a serializar
     * @param {*} format -> Formato de serialización 
     * @return {*} size -> tamaño de bits de la trama. buffer -> Node.js Buffer.
     * 
     */
     encode(_object, format) {
        //let _size = _object.size;
        const buffer = Buffer.alloc(3);
        //ToDo
        const size = 3;
        return { size, buffer };
    }

}

const format1 = [
		{ tag: "PTemp", type: "int", len: 12 },
		{ tag: "BattVolt.value", type: "int", len: 12 },
    	{ tag: "WaterLevel", type: "int", len: 8 },
	]; 
			
var data = { "PTemp": 268, "BattVolt.value": 224, "WaterLevel": 115 }; 
    
var bp = new BinaryParser();
var dataEncoded = bp.encode(data, format1); 
console.log(dataEncoded.buffer.toString('hex')); //prints 10C0E073
console.log(dataEncoded.size); //prints 32
var dataDecoded = bp.decode(dataEncoded.buffer, format1);
console.log(dataDecoded) //prints { PTemp: 268, ‘BattVolt.value’: 224, WaterLevel: 115 }
