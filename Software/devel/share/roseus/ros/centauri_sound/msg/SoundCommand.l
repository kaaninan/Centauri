;; Auto-generated. Do not edit!


(when (boundp 'centauri_sound::SoundCommand)
  (if (not (find-package "CENTAURI_SOUND"))
    (make-package "CENTAURI_SOUND"))
  (shadow 'SoundCommand (find-package "CENTAURI_SOUND")))
(unless (find-package "CENTAURI_SOUND::SOUNDCOMMAND")
  (make-package "CENTAURI_SOUND::SOUNDCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude SoundCommand.msg.html


(defclass centauri_sound::SoundCommand
  :super ros::object
  :slots (_cmd _param ))

(defmethod centauri_sound::SoundCommand
  (:init
   (&key
    ((:cmd __cmd) "")
    ((:param __param) "")
    )
   (send-super :init)
   (setq _cmd (string __cmd))
   (setq _param (string __param))
   self)
  (:cmd
   (&optional __cmd)
   (if __cmd (setq _cmd __cmd)) _cmd)
  (:param
   (&optional __param)
   (if __param (setq _param __param)) _param)
  (:serialization-length
   ()
   (+
    ;; string _cmd
    4 (length _cmd)
    ;; string _param
    4 (length _param)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _cmd
       (write-long (length _cmd) s) (princ _cmd s)
     ;; string _param
       (write-long (length _param) s) (princ _param s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _cmd
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _cmd (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _param
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _param (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get centauri_sound::SoundCommand :md5sum-) "0f57c5646299694f577923099e79540a")
(setf (get centauri_sound::SoundCommand :datatype-) "centauri_sound/SoundCommand")
(setf (get centauri_sound::SoundCommand :definition-)
      "string cmd
string param
")



(provide :centauri_sound/SoundCommand "0f57c5646299694f577923099e79540a")


