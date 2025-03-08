import { Button, Form, Input,Checkbox } from 'antd';
const { TextArea } = Input;

export default function ToneFormItems() {
  const toneOptions = [0,1,2,3,4,5,6,7,8,9];
  const onChange = (checkedValues) => {
    console.log('checked = ', checkedValues);
  };
  return <>
    <Form.Item label="单词" name="word">
      <Input placeholder="请输入" />
    </Form.Item>
    <Form.Item label="声调" name="tone">
      <Checkbox.Group
        options={toneOptions}
        onChange={onChange}
      />
    </Form.Item>
    <Form.Item label="假名" name="spell">
      <Input placeholder="请输入" />
    </Form.Item>
    <Form.Item label="含义" name="mean">
      <Input placeholder="请输入" />
    </Form.Item>
    <Form.Item label="句子" name="sentence">
      <TextArea rows={1} placeholder="请输入"/>
    </Form.Item>
    <Form.Item label="翻译" name="translate">
      <TextArea rows={1} placeholder="请输入"/>
    </Form.Item>
    <Form.Item label="备注" name="remark">
      <TextArea rows={4} placeholder="请输入"/>
    </Form.Item>
  </>
}