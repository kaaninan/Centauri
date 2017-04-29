
(cl:in-package :asdf)

(defsystem "centauri_sound-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SoundCommand" :depends-on ("_package_SoundCommand"))
    (:file "_package_SoundCommand" :depends-on ("_package"))
  ))