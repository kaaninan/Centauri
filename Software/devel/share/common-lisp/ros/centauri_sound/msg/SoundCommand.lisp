; Auto-generated. Do not edit!


(cl:in-package centauri_sound-msg)


;//! \htmlinclude SoundCommand.msg.html

(cl:defclass <SoundCommand> (roslisp-msg-protocol:ros-message)
  ((cmd
    :reader cmd
    :initarg :cmd
    :type cl:string
    :initform "")
   (param
    :reader param
    :initarg :param
    :type cl:string
    :initform ""))
)

(cl:defclass SoundCommand (<SoundCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SoundCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SoundCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name centauri_sound-msg:<SoundCommand> is deprecated: use centauri_sound-msg:SoundCommand instead.")))

(cl:ensure-generic-function 'cmd-val :lambda-list '(m))
(cl:defmethod cmd-val ((m <SoundCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader centauri_sound-msg:cmd-val is deprecated.  Use centauri_sound-msg:cmd instead.")
  (cmd m))

(cl:ensure-generic-function 'param-val :lambda-list '(m))
(cl:defmethod param-val ((m <SoundCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader centauri_sound-msg:param-val is deprecated.  Use centauri_sound-msg:param instead.")
  (param m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SoundCommand>) ostream)
  "Serializes a message object of type '<SoundCommand>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'cmd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'cmd))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'param))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'param))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SoundCommand>) istream)
  "Deserializes a message object of type '<SoundCommand>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cmd) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'cmd) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'param) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'param) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SoundCommand>)))
  "Returns string type for a message object of type '<SoundCommand>"
  "centauri_sound/SoundCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SoundCommand)))
  "Returns string type for a message object of type 'SoundCommand"
  "centauri_sound/SoundCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SoundCommand>)))
  "Returns md5sum for a message object of type '<SoundCommand>"
  "0f57c5646299694f577923099e79540a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SoundCommand)))
  "Returns md5sum for a message object of type 'SoundCommand"
  "0f57c5646299694f577923099e79540a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SoundCommand>)))
  "Returns full string definition for message of type '<SoundCommand>"
  (cl:format cl:nil "string cmd~%string param~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SoundCommand)))
  "Returns full string definition for message of type 'SoundCommand"
  (cl:format cl:nil "string cmd~%string param~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SoundCommand>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'cmd))
     4 (cl:length (cl:slot-value msg 'param))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SoundCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'SoundCommand
    (cl:cons ':cmd (cmd msg))
    (cl:cons ':param (param msg))
))
