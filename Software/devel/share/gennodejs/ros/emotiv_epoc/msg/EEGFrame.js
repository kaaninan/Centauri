// Auto-generated. Do not edit!

// (in-package emotiv_epoc.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class EEGFrame {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.accel_x = null;
      this.accel_y = null;
      this.channel_count = null;
      this.channel_names = null;
      this.signals = null;
      this.qualities = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('accel_x')) {
        this.accel_x = initObj.accel_x
      }
      else {
        this.accel_x = 0;
      }
      if (initObj.hasOwnProperty('accel_y')) {
        this.accel_y = initObj.accel_y
      }
      else {
        this.accel_y = 0;
      }
      if (initObj.hasOwnProperty('channel_count')) {
        this.channel_count = initObj.channel_count
      }
      else {
        this.channel_count = 0;
      }
      if (initObj.hasOwnProperty('channel_names')) {
        this.channel_names = initObj.channel_names
      }
      else {
        this.channel_names = [];
      }
      if (initObj.hasOwnProperty('signals')) {
        this.signals = initObj.signals
      }
      else {
        this.signals = [];
      }
      if (initObj.hasOwnProperty('qualities')) {
        this.qualities = initObj.qualities
      }
      else {
        this.qualities = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EEGFrame
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [accel_x]
    bufferOffset = _serializer.uint32(obj.accel_x, buffer, bufferOffset);
    // Serialize message field [accel_y]
    bufferOffset = _serializer.uint32(obj.accel_y, buffer, bufferOffset);
    // Serialize message field [channel_count]
    bufferOffset = _serializer.uint32(obj.channel_count, buffer, bufferOffset);
    // Serialize message field [channel_names]
    bufferOffset = _arraySerializer.string(obj.channel_names, buffer, bufferOffset, null);
    // Serialize message field [signals]
    bufferOffset = _arraySerializer.uint32(obj.signals, buffer, bufferOffset, null);
    // Serialize message field [qualities]
    bufferOffset = _arraySerializer.uint32(obj.qualities, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EEGFrame
    let len;
    let data = new EEGFrame(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [accel_x]
    data.accel_x = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [accel_y]
    data.accel_y = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [channel_count]
    data.channel_count = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [channel_names]
    data.channel_names = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [signals]
    data.signals = _arrayDeserializer.uint32(buffer, bufferOffset, null)
    // Deserialize message field [qualities]
    data.qualities = _arrayDeserializer.uint32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.channel_names.forEach((val) => {
      length += 4 + val.length;
    });
    length += 4 * object.signals.length;
    length += 4 * object.qualities.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'emotiv_epoc/EEGFrame';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '86134851c3839c35d0c7eb7049a290b2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    uint32 accel_x
    uint32 accel_y
    
    uint32 channel_count
    string[] channel_names
    uint32[] signals
    uint32[] qualities
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EEGFrame(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.accel_x !== undefined) {
      resolved.accel_x = msg.accel_x;
    }
    else {
      resolved.accel_x = 0
    }

    if (msg.accel_y !== undefined) {
      resolved.accel_y = msg.accel_y;
    }
    else {
      resolved.accel_y = 0
    }

    if (msg.channel_count !== undefined) {
      resolved.channel_count = msg.channel_count;
    }
    else {
      resolved.channel_count = 0
    }

    if (msg.channel_names !== undefined) {
      resolved.channel_names = msg.channel_names;
    }
    else {
      resolved.channel_names = []
    }

    if (msg.signals !== undefined) {
      resolved.signals = msg.signals;
    }
    else {
      resolved.signals = []
    }

    if (msg.qualities !== undefined) {
      resolved.qualities = msg.qualities;
    }
    else {
      resolved.qualities = []
    }

    return resolved;
    }
};

module.exports = EEGFrame;
