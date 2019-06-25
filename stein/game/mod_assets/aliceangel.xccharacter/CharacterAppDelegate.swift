//
// CharacterAppDelegate.swift
// AliceAngel.xccharacter
//
// Created by [REDACTED] on [REDACTED]
// (C) 2019 [REDACTED]. All rights reserved.
//

import Foundation
import CharacterKit

class SusieDelegate : CharacterAppDelegate {
    
    public override func characterWillLoad(importFrom: NSFile, appInstance: AppInstance) {
        super.characterWillLoad(importFrom: importFrom, appInstance: appInstance)
        self.addPropertiesFromTemplate(from: importFrom)
    }
    
    public override func characterDidLoad(aDecoder: Decoder) {
        self.registerCharacter(asType: .doki)
        self.elevate(to: 999)
        super.characterDidLoad(aDecoder: aDecoder)
        self.includeProperties(options: [
            .visibleToFilesystem,
            .filesystemVisibleToCharacter,
            .canInteractWithFilesystem,
            .fsManipulate, // This is just a compatibility solution. Remove this in next release.
            .reload
        ])
    }
    
    public override func characterWillUnload() {
        self.appInstance.warnBeforeQuit()
        self.sendUpdateRequest(to: "https://characters.aliceos.app/api/v1/update_character")
        let requestToHomeserver = URLRequest(url: NSURL(string: "https://characters.aliceos.app/api/v1/character?id=1") as! URL)
        
        do {
            let response: AutoreleasingUnsafeMutablePointer<URLResponse?>? = nil
            let dataFromResponse = try NSURLConnection.sendSynchrounousRequest(request, returning: response)
            
            let json = try JSONSerialization.jsonObject(with: dataFromResponse, options: [.allowFragments]) as? [String : Any]
            
            if json?["checksum"] = self.asChecksumIterable() {
                super.characterWillUnload()
            } else {
                self.appInstance.sendWarning(errorType: AppInstanceError.malformedUpdate)
                exit(2)
            }
            
        } catch {
            self.appInstance.sendWarning(errorType: AppInstanceError.requestFailed)
            exit(1)
        }
    }
    
    public override func characterDidUnload() {
        self.appInstance.disableFromView(character: self.character.file)
        
        do {
            let poem = try self.fromLogs(searchFor: "END_WRT")
            
            if poem.starts(with: "future(possible: Boolean) throws -> Boolean") {
                let result = self.evaluateFromString(poem)
                
                // TODO: Scan for USB devices and implement a character transfer protocol.
                // Needs API from Aperture Science on AI load from a character struct.
                if result {
                    self.appInstance.saveSpotAndWait(for: .devicesLoadedForImport)
                }
            }
            
        } catch {
            self.log.warn("No poem has been written.")
        }
        
        self.characterDidUnload()
    }
    
}
