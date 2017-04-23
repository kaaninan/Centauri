// Auto-generated. Do not edit!

// (in-package emotiv_epoc.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ChangeFrequencyRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.frequency = null;
    }
    else {
      if (initObj.hasOwnProperty('frequency')) {
        this.frequency = initObj.frequency
      }
      else {
        this.frequency = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ChangeFrequencyRequest
    // Serialize message field [frequency]
    bufferOffset = _serializer.uint32(obj.frequency, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ChangeFrequencyRequest
    let len;
    let data = new ChangeFrequencyRequest(null);
    // Deserialize message field [frequency]
    data.frequency = _deserializer.uint32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'emotiv_epoc/ChangeFrequencyRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '73ffa65309f649b8b694f03ce8799567';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint32 frequency
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ChangeFrequencyRequest(null);
    if (msg.frequency !== undefined) {
      resolved.frequency = msg.frequency;
    }
    else {
      resolved.frequency = 0
    }

    return resolved;
    }
};

class ChangeFrequencyResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ChangeFrequencyResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ChangeFrequencyResponse
    let len;
    let data = new ChangeFrequencyResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'emotiv_epoc/ChangeFrequencyResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ChangeFrequencyResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: ChangeFrequencyRequest,
  Response: ChangeFrequencyResponse,
  md5sum() { return '73ffa65309f649b8b694f03ce8799567'; },
  datatype() { return 'emotiv_epoc/ChangeFrequency'; }
};
