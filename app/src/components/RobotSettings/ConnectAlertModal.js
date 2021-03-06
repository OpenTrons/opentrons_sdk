// @flow
// AlertModal for failed connection to robot
import * as React from 'react'
import { useTranslation } from 'react-i18next'

import { AlertModal, Text } from '@opentrons/components'
import { Portal } from '../portal'
export type ConnectAlertModalProps = {|
  onCloseClick: () => mixed,
|}

export function ConnectAlertModal(props: ConnectAlertModalProps): React.Node {
  const { onCloseClick } = props
  const { t } = useTranslation('robot_connection')

  return (
    <Portal>
      <AlertModal
        heading={t('failed_connection_heading')}
        onCloseClick={onCloseClick}
        buttons={[{ onClick: onCloseClick, children: 'close' }]}
        alertOverlay
      >
        <Text>{t('failed_connection_body')}</Text>
      </AlertModal>
    </Portal>
  )
}
