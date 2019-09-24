//
// Override.swift
// Monika.xccharacter
//
// Created by [REDACTED] on [REDACTED]
// (C) 2019 [REDACTED]. All rights reserved.
//

import Foundation
import AsrielKit

class MonikaDelegate : ADCharacterDelegate {
    
    public override func characterWillLoad(importFrom: NSFile) {
        super.characterWillLoad(importFrom: importFrom)
        self.addPropertiesFromTemplate(from: importFrom)
    }
    
    public override func characterDidLoad(aDecoder: Decoder) {
        self.registerCharacter(asType: .dreemurr)
        self.elevate(to: 999)
        self.characterDidLoad(aDecoder: aDecoder)
        self.disable(options: [.asrielName, .hyperGoner, .floral])
        self.forceEnable(options: [.fireball, .reload, .fsManipulate])
    }
    
    // TODO: Implement characterWillUnload function.
    public override func characterWillUnload() { }
    
    // TODO: Implement characterDidUnload function
    public override func characterDidUnload() { }
    
}
